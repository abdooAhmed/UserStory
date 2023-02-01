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
                var iwantTo = $('<td class="align-middle text-center ">'+ element['iWantTO'] +'</td>')
                var soThat = $('<td class="align-middle text-center ">'+ element['soThat'] +'</td>')
                var epic = $('<td class="align-middle text-center ">'+ element['epic'] +'</td>')
                var priority = $('<td class="align-middle text-center ">'+ element['priority'] +'</td>')
                var devTask = $('<td class="align-middle text-center ">'+ element['devTask'].join() +'</td>')
                var RAIDS = $('<td class="align-middle text-center ">'+ element['RAIDS'].join() +'</td>')
                var persona = $('<td class="align-middle text-center ">'+ element['persona'].join() +'</td>')
                var row = $('<tr ></tr>')
                row.append(persona).append(epic).append(iwantTo).append(soThat).append(devTask).append(RAIDS);
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