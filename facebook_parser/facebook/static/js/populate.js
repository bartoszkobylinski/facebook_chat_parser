function populate(){
            
    var doc = document.getElementById('words-select');
    if (doc.value == "4 letters"){
        for(index = 0; index<doc.length; index ++){
            document.getElementsByClassName('hide-stat')[index].style.display = 'none'
        }
        document.getElementsByClassName('stats-4-words')[0].style.display = 'flex';
    }
    else if(doc.value == '5 letters'){
        for(index = 0; index<doc.length; index ++){
            document.getElementsByClassName('hide-stat')[index].style.display = 'none'
        }
        document.getElementsByClassName('stats-5-words')[0].style.display = 'flex';
    }
    else if(doc.value == '6 letters'){
        for(index = 0; index<doc.length; index ++){
            document.getElementsByClassName('hide-stat')[index].style.display = 'none'
        }
        document.getElementsByClassName('stats-6-words')[0].style.display = 'flex';
    }
    else if (doc.value == '7 letters'){
        for(index = 0; index<doc.length; index ++){
            document.getElementsByClassName('hide-stat')[index].style.display = 'none'
        }
        document.getElementsByClassName('stats-7-words')[0].style.display = 'flex';
    }
    else if(doc.value == '8 letters'){
        for(index = 0; index<doc.length; index ++){
            document.getElementsByClassName('hide-stat')[index].style.display = 'none'
        }
        document.getElementsByClassName('stats-8-words')[0].style.display = 'flex';
    }
    else if (doc.value == '9 letters'){
        for(index = 0; index<doc.length; index ++){
            document.getElementsByClassName('hide-stat')[index].style.display = 'none'
        }
        document.getElementsByClassName('stats-9-words')[0].style.display = 'flex';
    }
    else if(doc.value == '10 letters'){
        for(index = 0; index<doc.length; index ++){
            document.getElementsByClassName('hide-stat')[index].style.display = 'none'
        }
        document.getElementsByClassName('stats-10-words')[0].style.display = 'flex';
    }     
}

var file = false
function changeText(){    
    document.getElementById('id_chat_file')
    if(file == true){
        var button = document.getElementById('upload-button')
        button.value = "Uploading...";
        button.style.backgroundColor = "#00cc00" 
        }
    }
