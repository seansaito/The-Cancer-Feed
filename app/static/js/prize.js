var theForm = document.getElementById( 'theForm' );

new stepsForm( theForm, {
  onSubmit : function( form ) {
    // hide form
    classie.addClass( theForm.querySelector( '.simform-inner' ), 'hide' );
    var messageEl = theForm.querySelector( '.final-message' );
    messageEl.innerHTML = 'Thank you! Please wait a moment.';
    classie.addClass( messageEl, 'show' );

    $.ajax({
      url: "/feedback_answer",
      data: $("form").serialize(),
      type:"POST",
      success: function(data, textStatus) {
        if ($('input[name="q6"]').val() === "42") {
          window.location.replace("/prize")
        } else {
          window.location.replace("/index")
        }
      },
      error: function(error) {
        console.log(error);
      }
    });
  }
} );
