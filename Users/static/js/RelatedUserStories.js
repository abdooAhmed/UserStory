$('.PersonaRelated').on('change',function(e){
    $('.spinner-border').removeClass('d-none')
    var epic = $('.EpicRelated').val();
    $.ajax({
        url: "http://127.0.0.1:8000/Apis/relatedUserStory",
        type: "get",
        dataType: 'json', //send it through get method
        data: {  
            Persona: $(this).val(),
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
            });
            $('.spinner-border').addClass('d-none')
        },
        error: function (xhr) {
            $('.spinner-border').addClass('d-none')
            //Do Something to handle error
        }
    });
});


$('.EpicRelated').on('change',function(e){
    $('.relatedUserStory').empty();
    $('.spinner-border').removeClass('d-none')
    var personaStr = $('.PersonaRelated').val();
    console.log(personaStr);
    console.log($(this).val());
    $.ajax({
        url: "http://127.0.0.1:8000/Apis/relatedUserStory",
        type: "get",
        dataType: 'json', //send it through get method
        data: {  
            Persona:personaStr ,
            Epic:$(this).val()
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
            });
            $('.spinner-border').addClass('d-none')
        },
        error: function (xhr) {
            $('.spinner-border').addClass('d-none')
            //Do Something to handle error
        }
    });
});