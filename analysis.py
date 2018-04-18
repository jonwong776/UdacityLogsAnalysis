#!/usr/bin/python3

import psycopg2


def main():

    """

    Used to analyze a Postgres2 database containing logs for a news website

    Required Files:
        newsdata.sql: Postgres2 logs database

    """

    # Connecting to the database
    conn = psycopg2.connect(database="news")
    c = conn.cursor()

    print("\nLOG ANALYSIS REPORT\n")
    print("------------------------------\n")
    print("# Most Popular Articles of All Time\n")

    # SQL query producing top_articles view
    c.execute("CREATE VIEW top_articles AS (SELECT title, author, COUNT(*) AS num FROM log, articles WHERE log.path LIKE concat('%', articles.slug) GROUP BY title, author ORDER BY num DESC);")    # noqa

    # SQL query producing most popular articles of all time
    c.execute("SELECT * FROM top_articles LIMIT 3;")
    results = c.fetchall()

    for entry in results:
        print(entry[0] + " - " + str(entry[2]) + " views")

    print("\n# Most Popular Article Authors of All Time\n")

    # SQL query producing most popular authors of all time
    c.execute("SELECT name, SUM(num) AS total FROM authors, top_articles WHERE id = author GROUP BY name ORDER BY total DESC;")     # noqa
    results = c.fetchall()

    for entry in results:
        print(entry[0] + " - " + str(entry[1]) + " views")

    print("\n# Days with > 1% Request Errors\n")

    # SQL query producing request_errors view
    c.execute("CREATE VIEW request_errors AS (SELECT CAST(time AS date) AS dt, COUNT(*) AS error_count FROM log WHERE status = '404 NOT FOUND' GROUP BY dt);")     # noqa

    # SQL query producing request_total view
    c.execute("CREATE VIEW request_total AS (SELECT CAST(time AS date) AS dt, COUNT(*) AS total_count FROM log GROUP BY dt);")     # noqa

    # SQL query producing the number of days with >1% errors
    c.execute("SELECT * FROM (SELECT request_errors.dt, error_count, total_count, cast(error_count AS float) / total_count AS error_ratio FROM request_errors, request_total WHERE request_errors.dt = request_total.dt ORDER BY error_ratio DESC) AS request_ratio WHERE error_ratio > 0.01;")     # noqa
    results = c.fetchall()

    for entry in results:
        print(
            entry[0].strftime("%B %d, %Y") + " - " +
            str("{0:.1f}".format(entry[3] * 100)) + "% errors")

    conn.close()

if __name__ == '__main__':
    main()
