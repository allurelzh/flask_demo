function bindCaptchaBtnClick() {
    $("#captcha-btn").on("click", function (event) {
        var $this = $(this)   //这里的$this获取的是#captcha-btn
        var email = $("input[name='email']").val();
        console.log(email)
        if (!email) {
            alert("请输入邮箱！")
            return;
        }
        //通过js发送网络请求：ajax  Async JavaScript And XML(Json)
        $.ajax({
            url:"/user/captcha",
            method:"POST",
            data:{
                "email":email
            },
            success:function (res){
                var code = res['code'];
                if(code == 200){
                    //取消点击事件
                    $this.off("click");
                    var countdown = 60;
                    var timer = setInterval(function () {
                        countdown-=1;
                        if (countdown>0){
                            $this.text(countdown+"秒后重新发送");
                        }else{
                            $this.text("获取验证码");
                            //重新执行这个函数，重新绑定点击事件
                            bindCaptchaBtnClick();
                            //如果不需要倒计时了，那么就记得要清除倒计时，否则就会一直执行下去
                            clearInterval(timer);
                        }
                    },1000);
                    alert("验证码发送成功！");
                }else{
                    alert(res['message']);
                }
            }
        })
    });
}
//因为要对一个按钮进行执行操作，所以需要等网页文档全部加载完成之后再执行
$(function () {
    bindCaptchaBtnClick();
})