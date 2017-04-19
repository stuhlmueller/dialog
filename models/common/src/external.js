const assert = require('assert');
const _ = require('lodash');
const minimist = require('minimist');


function jsnew(ctor, a, b, c, d, e) {
  return new ctor(a, b, c, d, e);
}


function stringToAction(s) {
  var who = s[0];
  var i = s.indexOf(' ');
  var line = s.slice(i + 1); // Remove who
  var j = line.indexOf(' ');
  var what = line.slice(0, j);
  var content = line.slice(j + 1);
  return new Action({ who, what, content });  
}


class Action {

  constructor({ who, what, content }) {
    this.who = who;
    this.what = what;
    this.content = content;
  }

  toString() {
    if (this.content) {
      return `${this.who}: ${this.what} ${this.content}`;
    } else {
      return `${this.who}: ${this.what}`;
    }
  }

  toWords() {
    return [`${this.who}:`, this.what].concat(this.content ? this.content.split(' ') : [])
  }

}


class Workspace {

  constructor(tree) {
    assert.ok(_.isArray(tree));
    this.tree = tree;
  }

  add(address, content) {
    assert.ok(_.isString(address));
    assert.ok(_.isString(content));
    function _add(tree) {
      if (!_.isArray(tree)) {
        return tree;
      } else if (tree[0] === address) {
        return tree.concat([[content]]);
      } else {
        return tree.map((w) => { return _add(w); });
      }
    };
    return new Workspace(_add(this.tree));
  }

  update(action) {
    assert.ok(action instanceof Action);
    if (action.what === 'INIT') {
      return new Workspace([ 'root' ]);
    } else if (action.what === 'MSG') {
      return this;
    } else if (action.what === 'ADD') {
      var tmp = action.content.split(' ');
      assert.equal(tmp.length, 2);
      var address = tmp[0];
      var content = tmp[1];
      return this.add(address, content);
    } else {
      throw new Error(`Unknown action type: ${action}`);
    }
  }

  toWords() {
    return _.flattenDeep(this.tree);
  }

  toTree() {
    return this.tree;
  }

}


module.exports = {
  jsnew,
  Workspace,
  Action,
  stringToAction,
  minimist
};