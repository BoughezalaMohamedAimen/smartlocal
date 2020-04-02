$(document).ready(function(){

    // $('.make-commande').click(function(){
    //   $('.commande').find('.title').html($(this).find('h6').html())
    //   $('.commande').find('.icon-container').html($(this).find('.icon-container').html())
    //   $('.custom-overlay').fadeIn("slow");
    //   $('.commande').addClass('visible')
    // })
    // $('.custom-overlay').click(function(){
    //   $('.custom-overlay').fadeOut("slow");
    //   $('.commande').removeClass('visible')
    // })

    $('.change-etat').change(function(){
      $.get({
        url:"/chambres/commande/"+$(this).attr('data-item')+'/',
        success:function(data,statusText, xhr){

            if(xhr.status==200)
            $('.message b').html("action efectuée avec success")
            else
            $('.message b').html("veuillez réessayer")
            $('.message').fadeIn("slow")
            setTimeout(function(){$('.message').fadeOut("slow")},1500)
        }
      })
    })

    $('.commande-rideau').mousedown(function() {
              // commande/
              $.get({
                url:"/chambres/commande/"+$(this).attr('data-item')+"/"+$(this).attr('data-action'),
                success:function(data,statusText, xhr){

                    if(xhr.status==200)
                    $('.message b').html("action efectuée avec success")
                    else
                    $('.message b').html("veuillez réessayer")
                    $('.message').fadeIn("slow")
                    setTimeout(function(){$('.message').fadeOut("slow")},1500)
                }
              })
          })
                        .mouseup(function() {
                          $.get({
                            url:"/chambres/commande/"+$(this).attr('data-item')+"/3",
                            success:function(data,statusText, xhr){

                                if(xhr.status==200)
                                $('.message b').html("action efectuée avec success")
                                else
                                $('.message b').html("veuillez réessayer")
                                $('.message').fadeIn("slow")
                                setTimeout(function(){$('.message').fadeOut("slow")},1500)
                            }
                          })

        });
})
