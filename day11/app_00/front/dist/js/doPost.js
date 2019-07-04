function doPost(to, p,token) {
    //to:提交动作（action）,
   // p:参数
    var myForm = document.createElement("form");
    myForm.method = "post";
    myForm.action = to;
    for (var i in p) {
        var myInput = document.createElement("input");
        myForm.setAttribute("authenticity_token",token)
        myInput.setAttribute("name", i);  // 为input对象设置name
        myInput.setAttribute("value", p[i]);  // 为input对象设置value
        myForm.appendChild(myInput);
    }
    document.body.appendChild(myForm);
    myForm.submit();
    document.body.removeChild(myForm);
}
