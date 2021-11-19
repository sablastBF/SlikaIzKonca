class Graph{
    constructor(){
        this.elements = [];
        this.edge = [];
    }

    add(x){
        this.elements.push(x);
        this.edge.push([]);
    }

    addEdge(x, y){
        this.edge[x].push(y);
       // this.edge[y].push(x);
    }

    show(){
        this.elements.forEach(el => el.show());

        //console.log( this.edge.length);
        for(let i = 0; i < this.edge.length; i++){
            for (let j = 0; j < this.edge[i].length; j++){
                stroke(5);
                let nod1 = this.elements[i].get();
                let nod2 = this.elements[this.edge[i][j]].get();
                push();
                    stroke(0, 90);
                    strokeWeight(1);
                    line(nod1[0], nod1[1], nod2[0], nod2[1]);
                pop();
            } 
        }
    }
    showEL(){
        this.elements.forEach(el => el.show());
    }
}