#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0) {
      return {};
    } else if (h <= 0) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
