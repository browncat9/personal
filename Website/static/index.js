function deleteNode(noteId){

    fetch("/delete-note" , {

        method : "POST" ,
        body: JSON.stringify({nodeId : noteId})

    }).then((_res) => {

        window.location.href = "/";

    });
}

$(function(){


    // Module
    $("#lecturer_status").fadeOut()
    $("#student_status").fadeOut()
    $("#module_status").fadeOut()
    $("#account").fadeOut()
    $("#view_module").fadeOut()
    $("#student_credit").fadeOut()
    $("#assign_module").fadeOut()
    $("#content_assign_student").fadeOut()
    $("#content_all_student").fadeOut()


    $("#module_assign_status").on("click" , function(){

        console.log($(this).val());

        if ($(this).val() == "assign_student"){

            $("#content_assign_student").fadeIn()
            $("#content_all_student").fadeOut()

        }else{
            $("#content_assign_student").fadeOut()
            $("#content_all_student").fadeIn()

        }


    })

    $("#nav_notification").on("click" , function(){

        $("#notification").fadeIn()
        $("#student_status").fadeOut()
        $("#lecturer_status").fadeOut()
        $("#module_status").fadeOut()
        $("#account").fadeOut()
        $("#view_module").fadeOut()
        $("#assign_module").fadeOut()

        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")

    })

    $("#nav_lecturer").on("click" , function(){


        $("#lecturer_status").fadeIn()

        $("#student_status").fadeOut()

        $("#account").fadeOut()
        $("#notification").fadeOut()
        $("#module_status").fadeOut()
        $("#view_module").fadeOut()
        $("#assign_module").fadeOut()

        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")


    })

    $("#nav_student").on("click" , function(){

        $("#student_status").fadeIn()

        $("#lecturer_status").fadeOut()
        $("#account").fadeOut()
        $("#notification").fadeOut()
        $("#module_status").fadeOut()
        $("#view_module").fadeOut()
        $("#assign_module").fadeOut()

        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")

    })

    $("#nav_module").on("click" , function(){

        $("#module_status").fadeIn()

        $("#lecturer_status").fadeOut()
        $("#student_status").fadeOut()
        $("#account").fadeOut()
        $("#notification").fadeOut()
        $("#view_module").fadeOut()
        $("#assign_module").fadeOut()

        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")


    })

    $("#nav_account").on("click" , function(){

        $("#account").fadeIn()

        $("#student_status").fadeOut()
        $("#student_status").fadeOut()
        $("#notification").fadeOut()
        $("#module_status").fadeOut()
        $("#view_module").fadeOut()
        $("#assign_module").fadeOut()

        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")

    })

    $("#nav_view_module").on("click" , function(){

        $("#view_module").fadeIn()

        $("#student_status").fadeOut()
        $("#account").fadeOut()
        $("#lecturer_status").fadeOut()
        $("#notification").fadeOut()
        $("#module_status").fadeOut()
        $("#assign_module").fadeOut()

        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")

    })

    $("#nav_assign_module").on("click" , function(){


        $("#assign_module").fadeIn()

        $("#view_module").fadeOut()
        $("#student_status").fadeOut()
        $("#account").fadeOut()
        $("#lecturer_status").fadeOut()
        $("#notification").fadeOut()
        $("#module_status").fadeOut()

        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")

    })

// add student 
    $("#userrole").on("change" , function(){

        value = $(this).val();

        if(value == "student"){

            $("#student_credit").show()
            $("#enrollment_date_row").show()


        }else{
            $("#student_credit").hide()
            $("#enrollment_date_row").hide()

        }
    })
    // end Module
    

    

    // Lecturer
    $("#view_student").fadeOut()
    $("#mark_student").fadeOut()

    $("#nav_view").on("click" , function(){

        $("#view_student").fadeIn()

        $("#notification").fadeOut()
        $("#mark_student").fadeOut()

        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")

    })

    $("#nav_notification").on("click" , function(){

        $("#notification").fadeIn()

        $("#view_student").fadeOut()

        $("#mark_student").fadeOut()

        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")

    })

    $("#nav_mark").on("click" , function(){

        $("#mark_student").fadeIn()

        $("#view_student").fadeOut()
        $("#notification").fadeOut()

        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")

    })
    // end Lecturer


    // student
    $("#check_grade").fadeOut()
    $("#defer").fadeOut()

    $("#nav_student").on("click" , function(){

       $("#student_notification").fadeIn()

       $("#view_grade").fadeOut()
       $("#quit").fadeOut()

        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")

    })
    $("#nav_grade").on("click" , function(){

       $("#view_grade").fadeIn()

       $("#student_notification").fadeOut()
       $("#quit").fadeOut()

        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")

    })
    $("#nav_quit").on("click" , function(){

       $("#quit").fadeIn()

       $("#student_notification").fadeOut()
       $("#view_grade").fadeOut()

        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")

    })
    // end student


    // coordinator
    $("#view_all_student").fadeOut()
    $("#view_all_lecturer").fadeOut()
    $("#view_all_module").fadeOut()

    $("#nav_all_student").on("click" , function(){

        $("#view_all_student").fadeIn()

        $("#coordinator_notification").fadeOut()
        $("#view_all_lecturer").fadeOut()
        $("#view_all_module").fadeOut()

        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")

    })
    $("#nav_all_lecturer").on("click" , function(){

        $("#view_all_lecturer").fadeIn()
        $("#view_all_student").fadeOut()
        $("#coordinator_notification").fadeOut()
        $("#view_all_module").fadeOut()


        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")

    })
    $("#nav_all_module").on("click" , function(){

        $("#view_all_module").fadeIn()

        $("#view_all_lecturer").fadeOut()
        $("#view_all_student").fadeOut()
        $("#coordinator_notification").fadeOut()

        $(this).parents("ul").find("a").removeClass("active")
        $(this).addClass("active")

    })
    // end coordinator



})
