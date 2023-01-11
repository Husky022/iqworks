$(document).ready(function () {

      $('#object_type input:checkbox').click(function(){
          if ($(this).is(':checked')) {
              $('#object_type input:checkbox').not(this).prop('checked', false);
          }
      });


      $('#send-calculation').on('click',function(){
          $.ajax({
              data: {
                  'checked_base': $('input[name="chk-base"]:checked').serialize(),
                  'checked_secondary': $('input[name="chk-secondary"]:checked').serialize(),
                  'checked_type': $('input[name="chk-type"]:checked').serialize(),
                  'square': $('#square').val(),
                  'csrfmiddlewaretoken': csrf_token
                    },
              method: 'POST',
              url: '/get_calculation/',
              success: function (response) {
                  console.log(response.result)
                  $('.calc-result').html(response.result);
                  if (response.flag){
                      if (!$('.button-reset-calc').length){
                      $('#reset-calc').append($('<button class="button-reset-calc">Сбросить</button>'));
                      $('.result-note-after').html(
                          '<div class="result-after-note-text">' +
                              '<div>Примечание:</div>' +
                              '<div>1. Расчет яляется предварительным и не является конечным предложением, точная смета составляется только после выполнения проектных работ.</div>' +
                              '<div>2. Чтобы приблизить предварительный расчет к фактическому рекомендуем заполнить' +
                          ' <a href="#" class="questionnaire">опросный лист</a> и отправить нам или <a href="#"' +
                          ' class="calc-consultation" id="calc-consultation">обратиться к нам за' +
                          ' консультацией</a></div>' +
                          '</div>'
                          )
                      }
                  }


                }
          });
      });

      $('#reset-calc').on('click',function(){
          $.ajax({
              url: '/reset_calculation/',
              success: function () {
                  $('.calc-result').html('');
                  $('.result-note-after').html('');
                  $('input[name="chk-base"]:checked').prop('checked', false);
                  $('input[name="chk-secondary"]:checked').prop('checked', false);
                  $('input[name="chk-type"]:checked').prop('checked', false);
                  $('.button-reset-calc').remove()
                }
          });
      });
})


