CREATE TABLE "customers" (
  "customer_id" int PRIMARY KEY,
  "full_name" varchar,
  "phone" varchar
);

CREATE TABLE "orders" (
  "order_id" int PRIMARY KEY,
  "customer_id" varchar,
  "created_at" datetime
);

ALTER TABLE "orders" ADD FOREIGN KEY ("customer_id") REFERENCES "customers" ("customer_id");
