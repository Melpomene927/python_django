let gMsg = 'Hello~~~!!!!';
const PI = 3.1415926;

function Init(){
    //TESTPI();
    //TryLoop();
    //TryMath();
}

function TESTPI(){
    //alert(gMsg);
    let _radius = prompt('輸入半徑：');
    let _area = Math.pow(_radius, 2) * Math.PI;
    gMsg = '面積為：' + _area;
    $('#divMainArt').before($('<div />').addClass('alert alert-success').attr('role', 'alert').text(gMsg).append($('<button />').attr('type','button').attr('class','close').attr('data-dismiss','alert').attr('aria-label','close').append($('<span aria-hidden="true">&times;</span>'))));
}

function TryLoop(){
    let _arr = [];
    for(i = 0; i < 10; i++){
        _arr.push(i);
    }
    console.log(_arr);
    _arr.forEach(e => console.log(e ** 2));
}

function TryMath(){
    console.log(Math);
    let _rnd = Math.random();
    console.log(_rnd, Math.floor(_rnd * 10));
    let i=0, _max = 100, _min = 10, _arr = [], _pair = [];
    while(1){
        
        if (i%6 == 0 && i>0){
            _arr.push(_pair.slice(0, _pair.length));
            _pair = [];
        }
        _rnd = Math.floor(Math.random() * (_max - _min + 1)) + _min ;
        _pair.push(_rnd);
        //if(_rnd == 100) break;
        if(_arr.length >= 10) break;
        console.log(`第${++i}次: `, _rnd);
    }
    console.log(_arr);
}

$(document).ready(Init);
console.log('ready.');