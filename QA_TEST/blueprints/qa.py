from flask import Blueprint,render_template,request,g,redirect,url_for,flash
from decorators import login_required
from .forms import QuestionForm,CommentForm
from models import QuestionModel,AnswerModel
from exts import db
from sqlalchemy import or_
bp = Blueprint("qa",__name__,url_prefix="/")
@bp.route("/")
def index():
    questions = QuestionModel.query.order_by(db.text("-create_time")).all()
    return render_template("index.html",questions = questions)

#问答详情页面，在详情页面可以根据内容进行评论
@bp.route("/question/<int:id>")
def question_detail(id):
    question = QuestionModel.query.get(id)
    return render_template("detail.html",question=question)

@bp.route("/comment/<int:question_id>",methods=['POST'])
@login_required
def comment(question_id):
    form = CommentForm(request.form)
    if form.validate():
        content = form.content.data
        answer= AnswerModel(content =content,question_id=question_id,author =g.user)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for("qa.question_detail",id = question_id))
    else:
        flash("评论内容不能为空！")
        return redirect(url_for("qa.question_detail",id = question_id))



@bp.route("/question/public",methods=['GET','POST'])
@login_required
def public_question():
    #判断是否登录，如果没有登录，就跳转到登录页面
    if request.method == "GET":
        return render_template("public_question.html")
    else:
        form = QuestionForm(request.form)
        #验证成功以后就可以将数据存放到数据库中，这里需要先建立模型
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title,content=content,author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect("/")
        else:
            flash("标题或内容格式错误")
            return redirect(url_for("qa.public_question"))


@bp.route("/search")
def search():
    q = request.args.get("q")
    #filter_by：直接使用的是字段名称
    # filter:使用模型，字段名称
    questions = QuestionModel.query.filter(or_(QuestionModel.title.contains(q),QuestionModel.content.contains(q))).order_by(db.text("-create_time"))
    return render_template("index.html",questions=questions)
