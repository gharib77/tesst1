$(document).ready(function(){
    var loadform=function(){
        var btn=$(this)
        $.ajax({
            url:btn.attr("data-url"),
            type:'GET',
            dataType:'json',
            beforeSend: function () {
                $("#modal-client").modal("show");
              },
      
            success: function(data) {
                $("#modal-client .modal-content").html(data.html_form);
                $('#modal-client').modal('show');
            }
        })
    }

    var saveform = function(){
        var form=$(this)
        $.ajax({
            url:form.attr('action'),
            type:'POST',
            data:form.serialize(),
            dataType:'json',
            success:function(data){
                if(data.form_is_valid){
                    $("#table-client tbody").html(data.html_list_client)
                    $("#modal-client").modal('hide')
                }else{
                    $("#modal-client modal-content").html(data.html_form)

                }
            }
        })
        return false;
    }

    $(".js-create-pers").click(loadform)
    $("#modal-client").on('submit','.js-post-pers',saveform)

    $('.js-show-form-edit').click(loadform)
    $("#modal-client").on('submit','.js-update-form',saveform)






})