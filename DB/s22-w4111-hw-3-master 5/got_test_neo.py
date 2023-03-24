from neo4j import GraphDatabase

import config


def get_graph():
    g = GraphDatabase.driver(uri=config.neo_url,
                             auth=config.neo_auth
                             )
    return g


def t1():
    g = get_graph().session()
    q = "match (p:Person) where p.name=$name return p"
    res = g.run(q, {"name": "Tom Hanks"})
    print(type(res))
    for r in res:
        print(type(r))
        print(r)
        print("Labels = ", r['p'].labels)
        print("Properties = ", dict(r['p']))


if __name__ == "__main__":
    t1()
