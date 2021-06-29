
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

