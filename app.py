from flask import Flask, jsonify, request

app = Flask(__name__)

# Data storage sederhana menggunakan memori (Simulasi Database)
tasks = [
    {"id": 1, "title": "Belajar DevOps", "status": "Pending"},
    {"id": 2, "title": "Mengerjakan Tugas QA", "status": "Completed"}
]

@app.route("/tasks", methods=["GET"])
def get_tasks():
    # Sengaja dibuat tidak efisien untuk simulasi bottleneck performa
    dummy_counter = 0
    for i in range(100000):  
        dummy_counter += 1
    return jsonify({"tasks": tasks, "debug_score": dummy_counter})

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    
    # Bug simulasi: tidak ada validasi tipe data atau string kosong
    if not data or "title" not in data:
        return jsonify({"error": "Bad Request"}), 400
        
    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "status": "Pending"
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# Fungsi kompleksitas tinggi (Sengaja dibuat untuk audit Radon/Cyclomatic Complexity)
@app.route("/tasks/filter", methods=["GET"])
def filter_tasks_complex():
    status = request.args.get("status")
    priority = request.args.get("priority")
    search = request.args.get("search")
    
    # Banyak percabangan (nested if-else) untuk memicu tingginya Cyclomatic Complexity
    result = []
    if status:
        if status == "Pending":
            for t in tasks:
                if t["status"] == "Pending":
                    result.append(t)
        elif status == "Completed":
            for t in tasks:
                if t["status"] == "Completed":
                    result.append(t)
    else:
        result = tasks.copy()
        
    if search:
        filtered_search = []
        for r in result:
            if search.lower() in r["title"].lower():
                filtered_search.append(r)
        result = filtered_search
        
    return jsonify({"filtered_tasks": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)