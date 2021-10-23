var isValid = function(s) {
    var m = { '(' : ')', '[' : ']', '{' : '}' }
  var l = []
  for(var i of s){
    if(m[i]){
      l.push(i);
    }else{
      if(i != m[l.pop()]){
        return false;
      }
    }
  }
  return l.length == 0;
  
}
    
