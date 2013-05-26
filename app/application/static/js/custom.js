$(document).ready(function(){
  console.log( "The document got loaded!" );

  dima_reacts = function(){
        var thecommand = $("#dima-query").val();

        $.ajax({
            url:'./api/query',
            data:'{"query":"'+thecommand+'"}',
            type:'POST',
            headers: {"Content-type": "application/json"},
            success:function(data) {
                console.log('Received response! ');
                window.theresponse = data;
                eval('dicty='+data+';');
                var view = {
                    flaky_in: thecommand,
                    flaky_out: window.theresponse
                };

                $("#dimasscreen").empty()
                for (var i=0;i < dicty.length;i++){
                    console.log('Hello: '+dicty[i]["line"]);
                    if (i%2 == 0) {
                        dima_paste = '<div class="row-fluid"><div class="span2">&nbsp;</div><div class="span8"><div class="span3  flaky-movie"><span class="text-center movietitle">'+ dicty[i]["movie"]+'</span></div><div class="span9  flaky-query"><p class="lead text-center">'+ dicty[i]["line"] +'</div></div><div class="span2">&nbsp;</div></div><div class="row-fluid"><div class="span2">&nbsp;</div><div class="span8 flaky-response"><p class="lead text-center">'+ dicty[i]["context"]+'</div><div class="span2">&nbsp;</div></div>';
                    } else {
                        dima_paste = '<div class="row-fluid"><div class="span2">&nbsp;</div><div class="span8">'+'<div class="span9  flaky-query"><p class="lead text-center">'+ dicty[i]["line"] +'</div>'+'<div class="span3  flaky-movie"><span class="text-center movietitle">'+ dicty[i]["movie"]+'</span></div>'+'</div><div class="span2">&nbsp;</div></div><div class="row-fluid"><div class="span2">&nbsp;</div><div class="span8 flaky-response"><p class="lead text-center">'+ dicty[i]["context"]+'</div><div class="span2">&nbsp;</div></div>';
                    }

                    $("#dimasscreen").prepend(dima_paste);
                }
                }
        });

    }

  $("#button-prompt").click(dima_reacts);

  $(document).keypress(function(e) {
    if(e.which == 13) {
        event.preventDefault();
        dima_reacts();
    }
});



});