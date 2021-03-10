//p1
//ヒーロー
//ヒロパの使用有無
//体力
//デッキ枚数
//秘策数
//秘策s↓
//手札枚数
//手札↓
//ボードミニオン数
//ボードミニオンs↓
//p2 以下略


String filename="../board.txt";
HashMap <String, Integer> cards;
PImage[] img;

class Board {
}
void setup() {
  size(1200, 800);
  cards = new HashMap<String, Integer>();
  img = new PImage[30];
  cards.put("SCH_617", 0);
  cards.put("SCH_312", 1);
  cards.put("DRG_253", 2);
  cards.put("SCH_133", 3);
  cards.put("SCH_231", 4);
  cards.put("SCH_600", 5);
  cards.put("BT_213", 6);
  cards.put("DRG_252", 7);
  cards.put("EX1_611", 8);
  cards.put("ULD_152", 9);
  cards.put("EX1_610", 10);
  cards.put("BT_203", 11);
  cards.put("SCH_142", 12);
  cards.put("EX1_536", 13);
  cards.put("EX1_539", 14);
  cards.put("NEW1_031", 15);
  cards.put("DRG_256", 16);
  cards.put("SCH_428", 17);
  img[0] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/a4a65340aec0417bcf37598db81ec288ce84a11254ad1a771a9897be2a975d2d.png");
  img[1] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/7e5e80517f5309ed9a70414d3486a9828ca0e65086cebe9193019d50e9ac50f4.png");
  img[2] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/265840b3b55166099c6b7d4080085accec201f9100bb38e8878f05a2662d7568.png");
  img[3] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/7e753acc3f8e4b934d6ca4ba54fbcaad0f5814178999031b2e2312516f72bde1.png");
  img[4] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/9000c38a2d716465ebad64d168ab567d00c2a9e9fec30ef1cab294522f0576c9.png");
  img[5] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/9c26ec5418bc80c9bbd5729f57bf9c9ad69984adba2fed661f2c89287f757ecb.png");
  img[6] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/2de65933568d412dc2924127c3f2accddb1e40228001762324781d2ac99657b7.png");
  img[7] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/f48bbd2a1e45d3928f53b862bf4bd08a7eba209968b720eef6e4bf17d0dcbc16.png");
  img[8] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/4c389322adef82d46fe55bd528e0a87c619fcf8542ef1c562e293f916d4d939c.png");
  img[9] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/5aaf153bbfb128e461b86e6ba3925cb4e44d3a06b748a6c2e4c5d173e8b4d404.png");
  img[10] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/73da186010fc887dc705de5181a7e8f9aead05af8a976d8bdc58bb32d940b371.png");
  img[11] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/cdc82dad0d3e273519e0d8a5721c353c00e86f95c52b0c1f561af0dd95a71140.png");
  img[12] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/1a94dddaf84bfdf9d50277b78f4cae4c7de2f510fad09a599c733361b3785964.png");
  img[13] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/272f54459eb040c5fb514d5c496443ccbabb663161f0b17b70e81d07a06c0bb1.png");
  img[14] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/67bda939f725774e5a2fdd14312664040ab890f48ea286d6ee998103d9416974.png");
  img[15] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/211f28598cc1c3b707d39a43a1eee21d3b6e49f22bb09fdc4fb2a59f7fb82279.png");
  img[16] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/370a9d81d15897d9c23558b9812efe5e8429903fdde0655da7e5d4ce8092bc98.png");
  img[17] =loadImage("https://d15f34w2p8l1cc.cloudfront.net/hearthstone/6499ce4581606305ce931d0a3f0edd5ac28c4771ae8ec3cec03be671c43d15cd.png");




}
void draw() {
  //background(255);
  image(img[cards.get("SCH_600")].get(100, 100, 150, 150), 0, 0, width/10, width/10*1.39);
  if (frameCount%60==0) {
    update();
  }
}
void update() {
  String[] data = loadStrings(filename);
  for(int i=0;i<int(data[5]);i++){
    image(img[cards.get(data[i+6])], 0+i*50, 0, width/10, width/10*1.39);
  }
}
