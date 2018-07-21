    function func(self){
        console.log(self)
        alert(1234)
    }

    var ele = document.getElementsByTagName('div')[0]
    ele.onclick= function () {
        console.log(this)
    }

