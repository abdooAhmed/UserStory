var csrftoken = $("[name=csrfmiddlewaretoken]").val();
$('.updatePersona').change(function(e){
    console.log(this)
    var personaId = e.target.getAttribute('data-id');
    var persona = e.target.value;
    var userStoryId = $(this).closest('tr').attr('id');
    console.log(window.location.origin);
    if(personaId){
        $.ajax({
        url: "" + window.location.origin + "/Apis/editPersona/" + personaId + "",
        type: "PUT", //send it through get method
        contentType: 'application/json',
        headers:{
           "X-CSRFToken": csrftoken
        },  
        data: JSON.stringify({'persona':persona}),
        success: function (response) {
            console.log(response)
        },
        error: function (xhr) {
            alert("Error happenedy");
            //Do Something to handle error
        }
    });
    }
});

function addPersona(e){
    var userStoryId = $(e.target).closest('tr').attr('id');
    var persona = e.target.value;
     $.ajax({
        url: "" + window.location.origin + "/Apis/addPersona/" + userStoryId + "",
        type: "POST", //send it through get method
        contentType: 'application/json',
        headers:{
           "X-CSRFToken": csrftoken
        },  
        data: JSON.stringify({'persona':persona}),
        success: function (response) {
            console.log(response)
        },
        error: function (xhr) {
            alert("Error happenedy");
            //Do Something to handle error
        }
    });
}

$('.updateDevTask').change(function(e){
    var devTaskId = e.target.getAttribute('data-id');
    var devTask = e.target.value;
    var userStoryId = $(this).closest('tr').attr('id');
    if(devTaskId){
        $.ajax({
        url: "" + window.location.origin + "/Apis/editDevTask/" + devTaskId + "",
        type: "PUT", //send it through get method
        contentType: 'application/json',
        headers:{
           "X-CSRFToken": csrftoken
        },  
        data: JSON.stringify({'devTask':devTask}),
        success: function (response) {
            console.log(response)
        },
        error: function (xhr) {
            alert("Error happenedy");
            //Do Something to handle error
        }
    });
    }
});

function addDevTask(e){
    var userStoryId = $(e.target).closest('tr').attr('id');
    var devTask = e.target.value;
     $.ajax({
        url: "" + window.location.origin + "/Apis/addDevTask/" + userStoryId + "",
        type: "POST", //send it through get method
        contentType: 'application/json',
        headers:{
           "X-CSRFToken": csrftoken
        },  
        data: JSON.stringify({'devTask':devTask}),
        success: function (response) {
            console.log(response)
        },
        error: function (xhr) {
            alert("Error happenedy");
            //Do Something to handle error
        }
    });
}


$('.updateRaids').change(function(e){
    var raidsId = e.target.getAttribute('data-id');
    var raids = e.target.value;
    var userStoryId = $(this).closest('tr').attr('id');
    if(raidsId){
        $.ajax({
        url: "" + window.location.origin + "/Apis/editRaids/" + raidsId + "",
        type: "PUT", //send it through get method
        contentType: 'application/json',
        headers:{
           "X-CSRFToken": csrftoken
        },  
        data: JSON.stringify({'raids':raids}),
        success: function (response) {
            console.log(response)
        },
        error: function (xhr) {
            alert("Error happenedy");
            //Do Something to handle error
        }
    });
    }
});

function addRaids(e){
    var userStoryId = $(e.target).closest('tr').attr('id');
    var raids = e.target.value;
     $.ajax({
        url: "" + window.location.origin + "/Apis/addRaids/" + userStoryId + "",
        type: "POST", //send it through get method
        contentType: 'application/json',
        headers:{
           "X-CSRFToken": csrftoken
        },  
        data: JSON.stringify({'raids':raids}),
        success: function (response) {
            console.log(response)
        },
        error: function (xhr) {
            alert("Error happenedy");
            //Do Something to handle error
        }
    });
}

$('.updateUserStory').change(function(e){
    var name = e.target.getAttribute('data-name');
    var value = e.target.value;
    var userStoryId = $(this).closest('tr').attr('id');
    $.ajax({
        url: "" + window.location.origin + "/Apis/editUserStory/" + userStoryId + "",
        type: "PUT", //send it through get method
        contentType: 'application/json',
        headers:{
           "X-CSRFToken": csrftoken
        },  
        data: JSON.stringify({'name':name,'value':value}),
        success: function (response) {
            console.log(response)
        },
        error: function (xhr) {
            alert("Error happenedy");
            //Do Something to handle error
        }
    });
});

$('.updateEstimate').change(function(e){
    var estimateId = e.target.getAttribute('data-id');
    var estimate = e.target.value;
    $.ajax({
        url: "" + window.location.origin + "/Apis/editEstimate/" + estimateId + "",
        type: "PUT", //send it through get method
        contentType: 'application/json',
        headers:{
           "X-CSRFToken": csrftoken
        },  
        data: JSON.stringify({'estimate':estimate}),
        success: function (response) {
            console.log(response)
        },
        error: function (xhr) {
            alert("Error happenedy");
            //Do Something to handle error
        }
    });
});



function addEstimate(e){
    var estimate = e.target.value;
    var userStoryId = $(e.target).closest('tr').attr('id');
    var id = e.target.id
    $.ajax({
        url: "" + window.location.origin + "/Apis/addEstimate/" + userStoryId + "",
        type: "Post", //send it through get method
        contentType: 'application/json',
        headers:{
           "X-CSRFToken": csrftoken
        },  
        data: JSON.stringify({'estimate':estimate,'id':id}),
        success: function (response) {
            console.log(response)
        },
        error: function (xhr) {
            alert("Error happenedy");
            //Do Something to handle error
        }
    });
}