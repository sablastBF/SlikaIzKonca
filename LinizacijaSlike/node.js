class Node{
    constructor(x, y, idd){
        this.x = x;
        this.y = y;
        this.idd = idd
    }
    get(){
        return [this.x , this.y];
    }
    show() {
        fill(0, 0, 0);
        strokeWeight(1);
        textSize(10);
        text(this.idd, this.x, this.y);
        ellipse(this.x, this.y, 5, 5);
    }
}