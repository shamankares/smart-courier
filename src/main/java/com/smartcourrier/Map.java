package com.smartcourrier;

import java.awt.Graphics2D;

public class Map {
    BlokType[][] _blok;

    public Map(int size) {
        _blok = new BlokType[size][size];

    }

    public void drawMap(Graphics2D g){

    }
}

enum BlokType {
    HOME,
    STREET;
}