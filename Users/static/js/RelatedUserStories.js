$('.relatedUserStory').on('change',function(){
    var epics = Array.from($('.epicInputDetails'));
    console.log(epics)
    epicsValue =[]
    epics.forEach(ep=>{
        epicsValue.push(ep.value)
    })
    var personas = Array.from($('.peronsaInputDetails'));
    personasValue = []
    personas.forEach(ep=>{
        personasValue.push(ep.value)
    })
    relatedUserStory(epicsValue,personasValue);
})
function relatedUserStory(epics,personas){
    $('.relatedUserStory').empty();
    
    var index =0;
    if(epics.length>personas.length){
        index = epics.length;
    }
    else{
        index = personas.length;
    }
    for(var i=0;i<index;i++){
        var epic = "";
        var personaStr = "";
        if(i<epics.length){
            epic = epics[i];
        }
        if(i<personas.length){
            personaStr = personas[i];
        }
        $('.spinner-border').removeClass('d-none')
        $.ajax({
        url: "" + window.location.origin + "/Apis/relatedUserStory",
        type: "get",
        dataType: 'json', //send it through get method
        data: {  
            Persona:personaStr ,
            Epic:epic
        },
        success: function (response) {
            console.log(typeof response);
            data = JSON.parse(response);
            console.log(data[0]);
            if(data){
                var table = $('.d-none')
                table.removeClass('d-none')
                table.addClass('d-block')
            }
            else{
                var table = $('.d-block')
                table.removeClass('d-block')
                table.addClass('d-none')
            }
            data.forEach(element => {

                var iwantTo = $('<td class="align-middle text-center cursor-pointer" id="iWantTO" style="min-width: 16.5rem;">'+ element['iWantTO'] +'</td>')
                var soThat = $('<td class="align-middle text-center cursor-pointer" id="soThat" style="min-width: 16.5rem;">'+ element['soThat'] +'</td>')
                var epic = $('<td class="align-middle text-center cursor-pointer" id="epic" style="min-width: 16.5rem;">'+ element['epic'] +'</td>')
                var priority = $('<td class="align-middle text-center cursor-pointer" id="priority">'+ element['priority'] +'</td>')
                var devTask = $('<td class="align-middle text-center cursor-pointer" id="devTask" style="min-width: 31.5rem ;">'+ element['devTask'].join() +'</td>')
                var RAIDS = $('<td class="align-middle text-center cursor-pointer" id="RAIDS" style="min-width: 31.5rem ;">'+ element['RAIDS'].join() +'</td>')
                var persona = $('<td class="align-middle text-center cursor-pointer" id="persona" style="min-width: 16.5rem;">'+ element['persona'].join() +'</td>')
                var row = $('<tr onclick=selectUserStory(event,this)></tr>')
                row.append($('<td></td>')).append(persona).append(epic).append(iwantTo).append(soThat).append(devTask).append(RAIDS);
                $('.relatedUserStory').append(row);
                $('.spinner-border').addClass('d-none')
                $('.spinner-border').removeClass('d-block')
            });
        },
        error: function (xhr) {
            $('.spinner-border').addClass('d-none')
            $('.spinner-border').removeClass('d-block')
            //Do Something to handle error
        }
    });
    }
    $('.spinner-border').addClass('d-none')
    $('.spinner-border').removeClass('d-block')
}

function selectUserStory(e){
    var element = $(e.target);
    if(e.target.tagName == "TD")
    {
        element = $(e.target.parentNode);
    }
    var children = element.children();
    for(var i =0;i<children.length;i++){
        switch (children[i].id) {
        case 'iWantTO':
            $('.currentInput[name="IWantTO"]').val(children[i].textContent);
            $('.currentInput[name="IWantTO"]').val(function (i, val) {
                    return val + "\n";
                });
                if (!$('.currentInput[name="IWantTO"]').val()) {
                    e.target.style.height = 'auto';
                }
                else {
                    $('.currentInput[name="IWantTO"]').css("cssText", "height: " + $('.currentInput[name="IWantTO"]').prop("scrollHeight") + "px !important;");
            }
            break;
        case 'soThat':
            $('.currentInput[name="SoThat"]').val(children[i].textContent);
            $('.currentInput[name="SoThat"]').val(function (i, val) {
                    return val + "\n";
                });
                if (!$('.currentInput[name="SoThat"]').val()) {
                    e.target.style.height = 'auto';
                }
                else {
                    $('.currentInput[name="SoThat"]').css("cssText", "height: " + $('.currentInput[name="SoThat"]').prop("scrollHeight") + "px !important;");
            }
            break;
        case 'epic':
            $('.currentInput[name="Epic"]').val(children[i].textContent);
            $('.currentInput[name="Epic"]').val(function (i, val) {
                    return val + "\n";
                });
                if (!$('.currentInput[name="Epic"]').val()) {
                    e.target.style.height = 'auto';
                }
                else {
                    $('.currentInput[name="Epic"]').css("cssText", "height: " + $('.currentInput[name="Epic"]').prop("scrollHeight") + "px !important;");
            }
            break;
        case 'priority':
            $('.currentInput[name="Epic"]').val(children[i].textContent);
            break;
        case 'persona':
            $('.currentInput[name="Persona"]').val(children[i].textContent);
            $('.currentInput[name="Persona"]').val(function (i, val) {
                    return val + "\n";
                });
                if (!$('.currentInput[name="Persona"]').val()) {
                    e.target.style.height = 'auto';
                }
                else {
                    $('.currentInput[name="Persona"]').css("cssText", "height: " + $('.currentInput[name="Persona"]').prop("scrollHeight") + "px !important;");
            }
            break;
        case 'RAIDS':
            $('.currentInput[name="RAIDS"]').val(children[i].textContent);
            $('.currentInput[name="RAIDS"]').val(function (i, val) {
                    return val + "\n";
                });
                if (!$('.currentInput[name="RAIDS"]').val()) {
                    e.target.style.height = 'auto';
                }
                else {
                    $('.currentInput[name="RAIDS"]').css("cssText", "height: " + $('.currentInput[name="RAIDS"]').prop("scrollHeight") + "px !important;");
            }
            break;
        case 'devTask':
            $('.currentInput[name="Dev"]').val(children[i].textContent);
            $('.currentInput[name="Dev"]').val(function (i, val) {
                    return val + "\n";
                });
                if (!$('.currentInput[name="Dev"]').val()) {
                    e.target.style.height = 'auto';
                }
                else {
                    $('.currentInput[name="Dev"]').css("cssText", "height: " + $('.currentInput[name="Dev"]').prop("scrollHeight") + "px !important;");
            }
        }
    }
}