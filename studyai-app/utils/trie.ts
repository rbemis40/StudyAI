export type TrieData<T> = {
    name: string,
    value: T
};


class Node<T> {
    edges: Map<string, Node<T>>;
    values: T[];
    constructor() {
        this.edges = new Map();
        this.values = [];
    }

    followEdge(char: string): (Node<T> | undefined) {
        return this.edges.get(char);
    }

    addEdge(char: string, toNode: Node<T>): boolean {
        if (this.edges.get(char) !== undefined) {
            return false; // Edge alraedy exists
        }

        this.edges.set(char, toNode);
        return true;
    }

    addValue(newValue: T) {
        this.values.push(newValue);
    }
}

export class Trie<T> {
    root: Node<T>;

    constructor(initData: TrieData<T>[]) {
        this.root = new Node<T>();
        initData.forEach(data => this.addData(data));
    }

    addData(data: TrieData<T>) {
        let curNode = this.root;
        for(let char of data.name) {
            curNode.addValue(data.value);
            let nextNode = curNode.followEdge(char);
            if (!nextNode) {
                nextNode = new Node<T>();
                curNode.addEdge(char, nextNode);
            }

            curNode = nextNode;
        }

        curNode.addValue(data.value);
    }

    search(prefix: string): T[] {
        let curNode = this.root;
        for(let char of prefix) {
            let nextNode = curNode.followEdge(char)
            if (!nextNode) {
                return []; // The prefix is not in the trie
            }

            curNode = nextNode;
        }

        return curNode.values;
    }
}