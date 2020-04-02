$(document).ready(function(){

var hasbg=0;
  $('body').on('click','.openmenu',function(){
    $(this).removeClass('openmenu').addClass('closemenu');
    $(this).find('span').html('<i class="fa fa-times"></i>')
    $('section').css('transform','translateX(-25vw)');
    $('.menu').addClass('opened-menu');
    var time=100;
    $('.menu .link-child').each(function(){
          var ths=$(this);
          // alert(ths.html())
          setTimeout(function(){ths.removeClass('link-child-hidden');ths.removeClass('link-child-hidden-right')},time)
          time+=100;

    });
    $('nav').removeClass('bg-animated');
  });
  $('body').on('click','.closemenu',function(){

    // if($(this).hasClass('social'))
    // $('.link-child').addClass('link-child-hidden-left');
    // else
    $('.menu .link-child').addClass('link-child-hidden');

    $(this).removeClass('closemenu').addClass('openmenu');
    $(this).find('span').html('<i class="fa fa-bars"></i>')
    $('section').css('transform','translateX(0)');
    $('.menu').removeClass('opened-menu');
      if(hasbg==1)
    $('nav').addClass('bg-animated');
  });




})
