def hanoi(n, source, target, helper, moves=None):
    if moves is None: moves = []
    if n == 1:
        moves.append((source, target))
        print(f"  Disk 1: {source} → {target}")
        return moves
    hanoi(n-1, source, helper, target, moves)
    moves.append((source, target))
    print(f"  Disk {n}: {source} → {target}")
    hanoi(n-1, helper, target, source, moves)
    return moves

def hanoi_count(n):
    """n disk uchun minimal harakatlar soni = 2^n - 1"""
    return 2**n - 1

if __name__ == "__main__":
    for n in [2, 3, 4]:
        print(f"\n{n} ta disk:")
        moves = hanoi(n, "A", "C", "B")
        print(f"  Jami: {len(moves)} harakat (formula: {hanoi_count(n)})")
