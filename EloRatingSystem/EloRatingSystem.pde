// rating system

// Agent class
class Agent{
  int power;
  String name;
  float rate;
  float E;
  int dice(int k){
    return (int)random(k);
  }
  void init(int i){
    power = dice(i);
    name = str(i);
    rate = 1500;
  }
}

void comp(Agent a,Agent b){
  println(a.name +"VS"+ b.name);
  Agent winner;
  Agent loser;
  PCalculation(a,b);
  if(a.power < b.power){
    println("winner is" + b.name);
    winner = b;
    loser = a;
  }else if(b.power < a.power ){
    println("winner is" + a.name);
    winner = a;
    loser = b;
  }else{
    println("draw");
    //本当は引き分け処理が必要
    //実験にはいらないので省略
    return;
  }
  newRate(winner,loser);
  //println("winnner's rate is "  + winner.rate);
  //println("loser's rate is " + loser.rate);
}

void PCalculation(Agent X,Agent Y){
  X.E = 1/(1+ pow(10,(Y.rate-X.rate)/400));  
  Y.E = 1/(1+ pow(10,(X.rate-Y.rate)/400));
}

void newRate(Agent winner,Agent loser){
  winner.rate = winner.rate + 100*(1 - winner.E);
  loser.rate = loser.rate + 100*(0 - loser.E);
}

/*void RatingSort(Agent a[]){
  float Max = a[0].rate;
  Agent temp;
  for(int i = 1; i < a.length ; i ++){
    temp = a[i];
    if(Max < temp.rate){
      Max = temp.rate;
    }
  }
}*/

Agent a []= new Agent [10];

void setup(){
  for(int i = 0; i < a.length;i++){
    a[i] = new Agent();
    a[i].init(i);
  }
  for(int j = 0 ; j < a.length ; j ++){
    for(int k = 0; k < a.length ; k ++ ){
      if(k!= j) comp(a[j],a[k]);
    }
  }
  for(int i = 0 ; i < a.length ; i ++){
    println(a[i].name+"のレートは"+a[i].rate + "でpowerは" + a[i].power);
  }
}
