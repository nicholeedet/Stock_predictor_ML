-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/9eWn4j
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "stock" (
    "id" int   NOT NULL,
    "date" date   NOT NULL,
    "open" decimal   NOT NULL,
    "high" decimal   NOT NULL,
    "low" decimal   NOT NULL,
    "close" decimal   NOT NULL,
    CONSTRAINT "pk_stock" PRIMARY KEY (
        "id"
     )
);

