
$(function(){
    $('#addform').ajaxForm(function(data) {
        $('#jquery-loadmodal-js-body').html(data);

    });
});//ready