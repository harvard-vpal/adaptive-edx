// enable xblock to request the lti user id for sending problem result

$(document).ready(function(){
    var lti_user_id = $('#lti-user-id').data('lti_user_id');
    var iframe = document.getElementById('vpal-activity').contentWindow;
    window.addEventListener("message", respondWithLtiUserId, false);
    function respondWithLtiUserId(event){
        if (event.origin !== "https://courses.edx.org"){
            return;
        }
        event.source.postMessage(lti_user_id, event.origin);
    }
});
