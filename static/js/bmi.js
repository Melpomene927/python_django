let gMsg = 'Hello~~~!!!!';
const PI = 3.1415926;

const getBmi = (height, weight, point=2) => (weight / (height / 100) ** 2).toFixed(point);


const comments = [
    {"bmi":18.5, "comment":"體重過輕"},
    {"bmi":24, "comment":"健康體重"},
    {"bmi":27, "comment":"體重過重"},
    {"bmi":999, "comment":"肥胖"}
]

function Init(){

    const txtHeight = document.getElementById('height');
    const txtWeight = document.getElementById('weight');
    const frmBMI = document.getElementById('frmBMI');

    frmBMI.onsubmit = form_Validation;
    txtHeight.oninput = initial_Form;
    txtWeight.oninput = initial_Form;

}

function initial_Form(){
    $('.alert').alert('close');
}

function form_Validation(){
    //不進行Submit動作
    return false;
}

function getComment(bmi){
    if (isNaN(bmi)) return;
    let _index = comments.findIndex(e => e['bmi'] >= bmi);
    return comments[_index].comment;
}

function btnCalc_Click(){
    let _bmi = 0.0, _greeting = '';
    const txtName = document.getElementById('name');
    const txtHeight = document.getElementById('height');
    const txtWeight = document.getElementById('weight');

    _bmi = getBmi(txtHeight.value, txtWeight.value);
    if (isNaN(_bmi)) return;
    _comment = getComment(_bmi);
    _greeting = (txtName.value) ?txtName.value :'' ;
    let _str = `Hi ${_greeting} 你的BMI: ${_bmi}   ${_comment}`
    $('#divBtn').before($('<div />').addClass('alert alert-success mt-3').attr('role', 'alert').text(_str).append($('<button />').attr('type','button').attr('class','close').attr('data-dismiss','alert').attr('aria-label','close').append($('<span aria-hidden="true">&times;</span>'))));
}

$(document).ready(Init);
console.log('ready.');