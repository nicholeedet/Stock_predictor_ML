-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/9eWn4j
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "stock" (
    CREATE TABLE "stock" (
    id SERIAL,
    "stock_id" int   ,
    "date" varchar,
	"close" decimal   ,
    "open" decimal   ,
    "low" decimal   ,
    "high" decimal   );

    CONSTRAINT "pk_stock" PRIMARY KEY (
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

