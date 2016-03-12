
$(document).ready(function() {
    var fname = "aleksiy ";
    var lname = "kudelsky";

    // block repeats of the same call
    var disable = true;

        //expand logo
        $('#logo').mouseenter( function(){
        $('#logo').removeClass("bold")
            if(disable){
                disable = false;
                var i = 0;
                function loop(){
                    $('#logo').text(  fname.substring(0, i) + lname.substring(0,i) );
                    if(++i == fname.length + 1){
                        disable = true;
                        return;
                    }
                    window.setTimeout(loop, 50);
                }
            loop();
            }

        });



         $('#logo').mouseleave( function(){
            if(disable){
                disable = false;
                var i = fname.length;
                function delayedLoop(){
                    $('#logo').text(  fname.substring(0, i) + lname.substring(0,i) );
                    if(--i == 0){
                        $('#logo').addClass("bold")
                        disable = true;
                        return;
                    }
                    window.setTimeout(delayedLoop, 50);
                }
                delayedLoop();
                }
        });




});

