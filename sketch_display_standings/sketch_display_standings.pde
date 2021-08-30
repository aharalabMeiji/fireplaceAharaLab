int num_of_player=2;

String path="https://github.com/aharalabMeiji/fireplaceAharaLab/blob/1st_competition_fixed_deck/";
String filename = "standings.csv";

String[] line;

int[][] standings;
int[] win;
int[] lose;
int offset=50;
float  boxSize=100;
String[] name;

void setup() {
  LoadData();
  num_of_player = 5;
  boxSize = (width - 2f * offset ) / (num_of_player+5f);
  standings = new int[num_of_player][num_of_player];
  win = new int[num_of_player];
  lose = new int[num_of_player];
  name = new String[num_of_player];
  frameRate(1);//1fpm
  size(1100, 600);
}



void draw() {
  background(255);
  update();
  dispTable();
}

void LoadData() {
  line = loadStrings(path+filename);
}

void update() {
  LoadData();
  int number = line.length;
  if (number>num_of_player) {
    exit();
  }
  for (int n=0; n<number; n++) {
    String data = line[n];
    String[] elements = split(data, ",");
    name[n] = elements[0];
    for (int m=0; m<number; m++) {
      standings[n][m] = int(elements[m+1]);
    }
    win[n] = int(elements[number+1]);
    lose[n] = int(elements[number+2]);
  }
}

void dispTable() {
  for (int x=0; x<=num_of_player+5; x++) {
    if (x==1 || x==2) continue;
    if (x==0 || x==3 || x==3+num_of_player || x==5+num_of_player) {
      strokeWeight(3);
    } else {
      strokeWeight(1);
    }
    stroke(0);
    line(offset + x * boxSize, offset, offset + x * boxSize, offset + num_of_player * boxSize);
  }
  for (int y=0; y<=num_of_player; y++) {
    stroke(0);
    strokeWeight(1);
    line(offset, offset + y*boxSize, offset + (5+num_of_player) * boxSize, offset + y*boxSize);
  }
  textSize(boxSize*0.36);
  fill(0);
  for (int y=0; y<num_of_player; y++) {
    text(name[y], offset+boxSize*0.1, offset+y*boxSize+boxSize*0.66);
  }
  for (int y=0; y<num_of_player; y++) {
    for (int x=0; x<num_of_player; x++) {
      text(standings[y][x], offset+boxSize*0.2+(x+3)*boxSize, offset+y*boxSize+boxSize*0.66);
    }
  }
  for (int y=0; y<num_of_player; y++) {
    text(win[y], offset+boxSize*0.2+(num_of_player+3)*boxSize, offset+y*boxSize+boxSize*0.66);
    text(lose[y], offset+boxSize*0.2+(num_of_player+4)*boxSize, offset+y*boxSize+boxSize*0.66);
  }
}
