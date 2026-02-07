from sqlalchemy import text
from db.connection import engine


# --------------------------------------------------
# UNIVERSAL FORMATTER
# --------------------------------------------------

def format_laptops(laptops):

    if not laptops:
        return "❌ No laptops found."

    lines = []

    for i, lap in enumerate(laptops, start=1):

        storage = f"{lap['storage']}GB" if lap['storage'] else "N/A"

        lines.append(
            f"""
💻 Laptop {i}
{lap['brand']} {lap['name']}

💰 Price   : ₹{lap['price']}
🧠 RAM     : {lap['ram']}GB
💾 Storage : {storage}
⚙️ CPU     : {lap['cpu']}
-----------------------------
"""
        )

    return "\n".join(lines)


# --------------------------------------------------
# GENERIC DB RUNNER  ⭐ (VERY SENIOR PRACTICE)
# --------------------------------------------------

def run_query(query, params):
    try:
        with engine.connect() as conn:
            result = conn.execute(text(query), params)
            laptops = [dict(row._mapping) for row in result.fetchall()]
        return format_laptops(laptops)

    except Exception as e:
        return f"❌ Database error: {str(e)}"


# --------------------------------------------------
# SEARCH BY BUDGET
# --------------------------------------------------

def search_by_budget(budget: int):

    upper_limit = budget + 10000

    query = text("""
        SELECT brand, name, price, ram, storage, cpu
        FROM laptops
        WHERE price BETWEEN :budget AND :upper_limit
        ORDER BY price ASC
        LIMIT 10;
    """)

    with engine.connect() as conn:
        result = conn.execute(
            query,
            {"budget": budget, "upper_limit": upper_limit}
        )
        laptops = result.fetchall()

        # ⭐ fallback if too few
        if len(laptops) < 5:

            fallback_query = text("""
                SELECT brand, name, price, ram, storage, cpu
                FROM laptops
                WHERE price <= :upper_limit
                ORDER BY price DESC
                LIMIT 10;
            """)

            result = conn.execute(
                fallback_query,
                {"upper_limit": upper_limit}
            )
            laptops = result.fetchall()

    return format_laptops([dict(row._mapping) for row in laptops])



# --------------------------------------------------
# FILTER BY RAM
# --------------------------------------------------

def filter_by_ram(min_ram: int):

    ram_upper = min_ram * 2

    query = """
        SELECT brand, name, price, ram, storage, cpu
        FROM laptops
        WHERE ram BETWEEN :min_ram AND :ram_upper
        ORDER BY ram ASC, price ASC
        LIMIT 20;
    """

    laptops = run_query(query, {
        "min_ram": min_ram,
        "ram_upper": ram_upper
    })

    # ⭐ fallback if too few laptops
    if "No laptops found" in laptops:

        fallback_query = """
            SELECT brand, name, price, ram, storage, cpu
            FROM laptops
            WHERE ram >= :min_ram
            ORDER BY ram ASC
            LIMIT 20;
        """

        laptops = run_query(fallback_query, {
            "min_ram": min_ram
        })

    return laptops



# --------------------------------------------------
# BEST VALUE LAPTOPS
# --------------------------------------------------

def best_value_laptops(max_price: int):

    upper_limit = int(max_price * 1.20)

    query = """
        SELECT 
            brand,
            name,
            price,
            ram,
            storage,
            cpu,

            ROUND((
                (
                    (ram * 0.25) +

                    (
                        CASE
                            WHEN LOWER(cpu) LIKE '%i9%' THEN 9
                            WHEN LOWER(cpu) LIKE '%i7%' THEN 8
                            WHEN LOWER(cpu) LIKE '%i5%' THEN 6
                            WHEN LOWER(cpu) LIKE '%i3%' THEN 4
                            WHEN LOWER(cpu) LIKE '%ryzen 9%' THEN 9
                            WHEN LOWER(cpu) LIKE '%ryzen 7%' THEN 8
                            WHEN LOWER(cpu) LIKE '%ryzen 5%' THEN 6
                            ELSE 4
                        END * 0.45
                    ) +

                    ((CAST(storage AS NUMERIC) / 512) * 0.30)

                ) / price * 100000
            )::numeric, 2) AS value_score

        FROM laptops
        WHERE price <= :upper_limit
        AND ram >= 16
        ORDER BY value_score DESC
        LIMIT 20;
    """

    return run_query(query, {
        "upper_limit": upper_limit
    })




def gaming_laptops(max_price: int = 150000, limit: int = 20):

    upper_limit = int(max_price * 1.10)  # ⭐ smart buffer (10%)

    query = """
        SELECT 
            brand,
            name,
            price,
            ram,
            storage,
            cpu,

            ROUND(
                (
                    (ram * 0.3) +

                    (
                        CASE
                            WHEN name ILIKE '%RTX 4090%' THEN 10
                            WHEN name ILIKE '%RTX 4080%' THEN 9
                            WHEN name ILIKE '%RTX 4070%' THEN 8
                            WHEN name ILIKE '%RTX 4060%' THEN 7
                            WHEN name ILIKE '%RTX 4050%' THEN 6
                            WHEN name ILIKE '%RTX 3050%' THEN 5
                            WHEN name ILIKE '%GTX%' THEN 4
                            WHEN name ILIKE '%RX%' THEN 6
                            ELSE 2
                        END * 0.5
                    ) +

                    (
                        CASE
                            WHEN cpu ILIKE '%i9%' THEN 9
                            WHEN cpu ILIKE '%i7%' THEN 7
                            WHEN cpu ILIKE '%i5%' THEN 5
                            WHEN cpu ILIKE '%ryzen 9%' THEN 9
                            WHEN cpu ILIKE '%ryzen 7%' THEN 7
                            WHEN cpu ILIKE '%ryzen 5%' THEN 5
                            ELSE 3
                        END * 0.2
                    )

                ) / price * 100000
            ,2) AS gaming_score

        FROM laptops
        WHERE price BETWEEN :max_price AND :upper_limit
        AND ram >= 16
        AND (
            name ILIKE '%RTX%' OR
            name ILIKE '%GTX%' OR
            name ILIKE '%RX%' OR
            name ILIKE '%ROG%' OR
            name ILIKE '%TUF%' OR
            name ILIKE '%Legion%' OR
            name ILIKE '%Nitro%' OR
            name ILIKE '%Predator%'
        )

        ORDER BY gaming_score DESC
        LIMIT :limit;
    """

    return run_query(query, {
        "max_price": max_price,
        "upper_limit": upper_limit,
        "limit": limit
    })




# --------------------------------------------------
# QUICK TEST
# --------------------------------------------------

if __name__ == "__main__":
    print(search_by_budget(70000))
