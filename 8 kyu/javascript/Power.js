/**
 * Created by kaleemmf on 8/11/17.
 */
function numberToPower(number, power){
  // Code here
  let result=1;
  for(var i=1; i<=power;i++){
  result*=number;
  }
  return result;
}