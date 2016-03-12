
function addln(id, str){
    if( "" == str){
         $(".shell").append("<br id='l" + i + "'>");
    }else{
         $(".shell").append("<div class='white' id='l" + i +"'>" + str + "<\/div>");
    }
}


function printConsole(size , str, head, cur ,pos ){
    strcpy = str.slice( str.length - size , str.length )

    var header = size - 1;
    if (cur < size){
        header = cur;
    }

    strcpy[header] =  head + strcpy[header].substring(0, pos ) + '\u2588' + strcpy[header].substring(pos);
    $(".shell").replaceWith("<div class='shell'><\/div>")
     for (i=0; i < size; i++) {
      addln(i,strcpy[i]);
    }
}






function initArray(size){
    var str = [];
    for(i=0; i < size; i++){
        str.push("");
    }
    return str;
}

function doCmd(cmd){
    switch(cmd){
        case "clear":
            str = initArray(size);
            //-1 to account for ++ later
            curln = -1;
            break;


        case "whoami":
            println(user);
            break;

        default:
            println("Command is not found.")
            break;


    }
}

function println(line){
    curln++;
    str[curln] = line;
}


$(document).ready(function() {
    //globals
    size = 30;
    maxchars = 65;
    user = "guest"
    headstr = user + ":~$";
    str = initArray(size);
    curln = 0;
    var pos = 0;
    printConsole(size, str, headstr, curln , pos);



     //handle
     $(document).keydown( function (e) {
        var key = e.which
        switch(key){
            case 8:
                //backspace
                e.preventDefault();
                str[curln] = str[curln].substring(0, pos -1) + str[curln].substring(pos);
                if(pos > 0 ){
                    pos--;
                }
                break;
            case 37:
                //left
                pos--;
                if(pos < 0  ){
                    pos = 0;
                }
                break;

            case 39:
                //right
                 pos++;
                 if(pos > str[curln].length){
                    pos = str[curln].length;
                 }
                 break;
        }
        printConsole(size, str, headstr, curln, pos);
    });

    //on key press
    $(window).keypress(function(e) {
       var key = e.which;
        switch(key){
            //enter
            case 13:
                pos = 0;
                //save cmd and add headstr to start
                cmd = str[curln];
                str[curln] = headstr + str[curln];
                doCmd(cmd);
                //keep header for commands
                if(curln >= size - 1 ){
                    str.push("");
                }
                curln++;
                break;


            default:
                if(str[curln].length < maxchars){
                    str[curln] = str[curln].substring(0, pos )+  String.fromCharCode(key) + str[curln].substring(pos);
                    pos++;
                }
                break;
        }






       printConsole(size, str, headstr, curln , pos);
   });

});



