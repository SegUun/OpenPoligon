import p5 from "https://cdn.skypack.dev/p5@1.4.1";
export class GridUnit {
    constructor(edgeLength, center) {
        this.edgeLength = edgeLength;
        this.center = center;
        this.upperLeftCorner = {
            x: this.center.x - edgeLength / 2,
            y: this.center.y - edgeLength / 2,
        };
    }
}
let dividedGridUnits = [];
export class Grid {
    constructor(x, y, unitEdgeLength, repetition) {
        this.x = x;
        this.y = y;
        this.unitEdgeLength = unitEdgeLength;
        this.repetition = repetition;
        this.edgeLength = unitEdgeLength * repetition;
        this.centerPoints = this.generateCenterPoints(this.unitEdgeLength, this.repetition);
        this.units = this.generateGridUnit(this.centerPoints, this.unitEdgeLength);
        this.upperLeftPoint = { x: this.x, y: this.y };
        this.lowerRightPoint = {
            x: this.upperLeftPoint.x + this.edgeLength,
            y: this.upperLeftPoint.y + this.edgeLength,
        };
    }
    generateCenterPoints(unit, repetition) {
        let coordinates = [];
        for (let i = 0; i < repetition; i++) {
            for (let j = 0; j < repetition; j++) {
                coordinates = [
                    ...coordinates,
                    {
                        x: unit * i + unit / 2 + this.x,
                        y: unit * j + unit / 2 + this.y,
                    },
                ];
            }
        }
        return coordinates;
    }
    generateGridUnit(centerPoints, unitEdgeLength) {
        return centerPoints.map((p) => {
            return new GridUnit(unitEdgeLength, p);
        });
    }
    divide() {
        if (this.edgeLength < 500) {
            dividedGridUnits = [...dividedGridUnits, ...this.units];
            return;
        }
        this.units.map((unit) => {
            if (Math.floor(Math.random() * 100) >= 80) {
                dividedGridUnits = [...dividedGridUnits, unit];
                return;
            }
            const newRepetitions = [2, 4, 8];
            const newRepetition = newRepetitions[Math.floor(Math.random() * newRepetitions.length)];
            const newGrid = new Grid(unit.upperLeftCorner.x, unit.upperLeftCorner.y, unit.edgeLength / newRepetition, newRepetition);
            newGrid.divide();
        });
    }
}
export const sketch = (p) => {
    const canvasWidth = 1200;
    const canvasHeight = 800;
    class Upper {
        constructor(unit) {
            this.baseDelay = 0;
            this.alpha = 255;
            this.isStop = false;
            this.startCenter = unit.center;
            this.edgeLength = unit.edgeLength;
            this.currentPosition = Object.assign({}, this.startCenter);
            this.delay = p.random(100, 100);
            this.speed = p.random(2, 5);
        }
        restart() {
            this.baseDelay = p.frameCount;
            this.isStop = false;
        }
        move() {
            if (this.isStop || p.frameCount < this.delay + this.baseDelay) {
                return;
            }
            if (p.dist(this.startCenter.x, this.startCenter.y, this.currentPosition.x, this.currentPosition.y) <=
                (canvasHeight * 25) / this.edgeLength) {
                this.currentPosition = {
                    x: this.currentPosition.x + this.speed,
                    y: this.currentPosition.y - this.speed,
                };
                this.alpha -= this.speed;
            }
            
            else {
                this.isStop = true;
                this.currentPosition = Object.assign({}, this.startCenter);
                this.alpha = 255;
            }
        }
        display() {
            const element = document.querySelector('.animation')
            const style = getComputedStyle(element).backgroundColor
            if (style.length == 12) {
                p.fill(Number(style.slice(4, 5)), Number(style.slice(7, 8)), Number(style.slice(10, 11)), this.alpha);
            } else {
                p.fill(Number(style.slice(4, 7)), Number(style.slice(9, 12)), Number(style.slice(14, 17)), this.alpha);
            }

            p.push();
            p.translate(this.currentPosition.x, this.currentPosition.y);
            p.triangle(-this.edgeLength / 2, -this.edgeLength / 2, -this.edgeLength / 2 + this.edgeLength, -this.edgeLength / 2, -this.edgeLength / 2, -this.edgeLength / 2 + this.edgeLength);
            p.pop();
        }
    }
    let uppers = [];
    p.setup = () => {
        p.createCanvas(canvasWidth, canvasHeight);
        p.angleMode(p.DEGREES);
        p.noStroke();
        const repetition = 10;
        const unitEdgeLength = 500 / repetition;
        const grid = new Grid(250, 250, unitEdgeLength, repetition);
        grid.divide();
        dividedGridUnits.map((unit) => {
            uppers = [...uppers, new Upper(unit)];
        });
    };
    p.draw = () => {
        const element = document.querySelector('.animation2')
        const style = getComputedStyle(element).backgroundColor
        p.background(String(style))
        p.translate(canvasWidth / 2, canvasHeight / 2);
        p.rotate(45);
        p.translate(-canvasWidth / 2, -canvasHeight / 2);
        if (uppers.every((upper) => {
            return upper.isStop;
        })) {
            uppers.map((upper) => {
                upper.restart();
                upper.display();
            });
        }
        else {
            uppers.map((upper) => {
                upper.move();
                upper.display();
            });
        }
    };
};
new p5(sketch);