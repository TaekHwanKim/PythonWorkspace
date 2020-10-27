if(checklist.part){
    //     result = filter_data.filter(function(object){ // function에서 true 값을 반환하는 객체들이 배열에 담기게 된다.
    //         arr=[];
    //         if(checklist.rank){ //체크가 되었으니 
    //             arr.push(object.rank.indexOf(text) == 0)
    //         }
    //         if(checklist.compony){
    //             arr.push(object.company.toLowerCase().includes(text))
    //         }
    //         if(checklist.revenues){
    //             arr.push(object.revenues.indexOf(text) == 0)
    //         }
    //         if(checklist.profits){
    //             arr.push(object.profits.indexOf(text) == 0)
    //         }
    //         let checktrue = arr.find(function(check){
    //             return check === true;
    //         });
    //         return checktrue;
    //     });
    //     return result;    
    // }
    // //2. 일치검색 일 경우 == 사용
    // else{
    //     result = filter_data.filter(function(object, index, obj){ // function에서 true 값을 반환하는 객체들이 배열에 담기게 된다.
    //         arr=[];
    //         if(checklist.rank){ //체크가 되었으니 
    //             arr.push(object.rank == text)
    //         }
    //         if(checklist.compony){
    //             arr.push(object.company.toLowerCase() == text)
    //         }
    //         if(checklist.revenues){
    //             arr.push(object.revenues == text)
    //         }
    //         if(checklist.profits){
    //             arr.push(object.profits == text)
    //         }
    //         let checktrue = arr.find(function(check){
    //             return check === true;
    //         });
    //         return checktrue;
    //     });
    //     return result;    
    // }