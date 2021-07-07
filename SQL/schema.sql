-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/9eWn4j
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "stock" (
    id SERIAL,
    "stock_id" INT   NOT NULL,
    "date" date   NOT NULL,
    "close" decimal NOT NULL,
    "open" decimal   NOT NULL,
    "low" decimal   NOT NULL,
    "high" decimal   NOT NULL,
    CONSTRAINT "pk_cases" PRIMARY KEY (
        "id"
     )
);

CREATE TABLE "ticker" (
    "stock_id" int   NOT NULL,
    "name" varchar   NOT NULL,
    "symbol" varchar   NOT NULL,
    CONSTRAINT "pk_ticker" PRIMARY KEY (
        "stock_id"
     )
);

CREATE TABLE "predicted" (
    id SERIAL,
    "stock_id" int   NOT NULL,
    "close" decimal NOT NULL,
    "predictions" decimal NOT NULL,
    CONSTRAINT "pk_predicted" PRIMARY KEY (
        "id"
     )
);