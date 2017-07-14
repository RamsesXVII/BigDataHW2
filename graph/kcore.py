from neo4j.v1 import GraphDatabase, basic_auth


driver = GraphDatabase.driver("bolt://localhost", auth=basic_auth("neo4j", "**********"))
session = driver.session()

while True:
    queryToDelete="match (n:p)-[r:precede]-(m:ipNode) with n, count(r) as DegreeScore where DegreeScore<9 detach delete (n)"
    session.run(queryToDelete)

    queryToDeleteONode="match(n) where not (n)-[]-() delete n"
    session.run(queryToDeleteONode)

    queryToCount="match (n:p)-[r:precede]-(m:ipNode) with n, count(r) as DegreeScore where DegreeScore<9 return count(n) as count"
    results = session.run(queryToCount)

    for record in results:
        remaining=int(record["count"])

    print(remaining)
    print("************")

    if remaining==0:
        break

#    match (n:ipNode)-[r:precede]-(m:ipNode) with n, count(r) as DegreeScore where DegreeScore=1 delete detach (n) return count(n)

#match (n:ipNode)-[r:precede]-(m:ipNode) with n, count(r) as DegreeScore where DegreeScore>1 detach delete (n)
