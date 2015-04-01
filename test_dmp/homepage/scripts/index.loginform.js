/**
 * Created by Spencer on 3/4/2015.
 */
/**
 * Created by Spencer on 3/3/2015.
 */
$(function(){
    $('#loginform').ajaxForm(function(data) {
        $('#jquery-loadmodal-js-body').html(data);

    });
});//ready