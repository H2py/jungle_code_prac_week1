import functools
import inspect
import graphviz

# FunctionVisualizer 클래스 정의 (제공된 코드 그대로)
class FunctionVisualizer:
    def __init__(self):
        self.dot = graphviz.Digraph()
        self.call_stack = []
        self.call_count = 0
        self.start_order_counter = 0
        self.finish_order_counter = 0
        self.node_info = {}

    def visualize(self, func=None, *, param_names=None, show_execution_order=False):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                self.call_count += 1
                current_id = f"call_{self.call_count}"
                self.start_order_counter += 1
                self.node_info[current_id] = {"start_index": self.start_order_counter}
                func_name = func.__name__

                if param_names is not None:
                    arg_names = inspect.getfullargspec(func).args
                    arg_dict = dict(zip(arg_names, args))
                    arg_dict.update(kwargs)
                    filtered_args = {k: arg_dict[k] for k in param_names if k in arg_dict}
                    args_str = ", ".join(f"{k}={v!r}" for k, v in filtered_args.items())
                else:
                    args_str = ", ".join(repr(arg) for arg in args)
                    kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
                    args_str = args_str + (", " if args_str and kwargs_str else "") + kwargs_str

                label = f"{func_name}({args_str})"
                self.dot.node(current_id, label=label)

                if self.call_stack:
                    self.dot.edge(self.call_stack[-1], current_id)

                self.call_stack.append(current_id)
                result = func(*args, **kwargs)
                self.finish_order_counter += 1
                self.node_info[current_id]["finish_index"] = self.finish_order_counter

                start_idx = self.node_info[current_id]["start_index"]
                finish_idx = self.node_info[current_id]["finish_index"]
                order_idx_str = f"start at: {start_idx}\nfinish at:{finish_idx}\n" if show_execution_order else ""
                updated_label = f"{label}\n{order_idx_str}return: {result!r}"
                self.dot.node(current_id, label=updated_label)
                self.call_stack.pop()
                return result
            return wrapper
        if func is not None:
            return decorator(func)
        return decorator

    def render(self, filename="function_calls", format="png"):
        self.dot.render(filename, format=format, cleanup=True)
        return filename + "." + format

# FunctionVisualizer 인스턴스 생성
visualizer = FunctionVisualizer()

# merge_sort 함수에 데코레이터 적용
@visualizer.visualize(param_names=["arr"], show_execution_order=True)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:] 
    
    sortedLeft = merge_sort(leftHalf)
    sortedRight = merge_sort(rightHalf)
    
    return merge(sortedLeft, sortedRight)

# merge 함수에 데코레이터 적용
@visualizer.visualize(param_names=["left", "right"], show_execution_order=True)
def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# 메인 실행
unsortedArr = [3, 7, 6, -10, 15, 23.5, 55, -13]
sortedArr = merge_sort(unsortedArr)
print("Sorted Array:", sortedArr)

# 그래프를 PNG 파일로 렌더링
visualizer.render(filename="merge_sort_visualization")