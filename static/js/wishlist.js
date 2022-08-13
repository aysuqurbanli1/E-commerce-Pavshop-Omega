$(document).on('click',"#two",function(){
    var pid=$(this).attr('data-product');
    console.log(pid)
    if(!pid){
        window.location = `/login/?next=${window.location.pathname}`
    }
    

});


jQuery(document).ready(function($){
   
    var check=$("#one").attr('data-product-like');
    console.log(check)
    console.log(check)
    if (check=="True"){
        var vm=$(".add-wishlist");
        $(".add-wishlist").css("color","red");
        vm.addClass('remove').removeClass('add-wishlist');
        console.log("HHHHHHH")  
        
    }
    else if(check=="False"){
        console.log("False")
        var v=$(".remove");
        $(".remove").css("color",""); 
        v.addClass('add-wishlist').removeClass('remove');
        
        console.log("ISledi")

    }
   
});


$(document).on('click',".add-wishlist",function(){
    var pid=$(this).attr('data-product');

    var vm=$(this);
    if(!pid){
        window.location = `/login/?next=${window.location.pathname}`
    }
    
    $.ajax({
        url:"/add-wishlist",
        // type:"POST",
        data:{
            productversion:pid
        },
        dataType:'json',
        success:function(res){
            // console.log("AAAAAAAa")
            // console.log(res)
            if (res.bool==false){
                console.log(vm)
                vm.addClass('remove').removeClass('add-wishlist');
                $(".remove").css("color","red");
                // a=vm.addClass("text-danger");
                res.bool=true
                console.log("AAAAb")
                console.log(res.bool)
            }
            // else if (res.bool==true){
            //     // vm.addClass('add-wishlist').removeClass('remove bg-danger');
            //     res.bool=false
            //     console.log("AAAAb")
            // }

        }
    })
});





$(document).on('click',".remove",function(){
   var v=$(this);
   var pid=$(this).attr('data-product');
 
   v.addClass('add-wishlist').removeClass('remove');
   $(".add-wishlist").css("color","");
   console.log("AAAAAAe");
   $.ajax({
    url:"/delete",
    // type:"GET",
    data:{
        productversion:pid
    },
    dataType:'json',
    // success:function(res){
    //     // console.log("AAAAAAAa")
    //     // console.log(res)
    //     if (res.bool==true){
    //         // a=vm.addClass("text-danger");
    //         res.bool=false
    //         console.log("AAAAb")
    //         console.log(res.bool)
    //     }
    //     // else if (res.bool==true){
    //     //     // vm.addClass('add-wishlist').removeClass('remove bg-danger');
    //     //     res.bool=false
    //     //     console.log("AAAAb")
    //     // }

    // }
})
});

   

