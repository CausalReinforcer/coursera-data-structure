# python3
import bisect


class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time


class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_times = []

    def update(self, time):
        if self.finish_times:
            if self.finish_times[-1] <= time:
                self.finish_times = []
            else:
                new_start = bisect.bisect_right(self.finish_times, time)
                self.finish_times = self.finish_times[new_start:]

    def process_with_buffer(self, request):
        start_time = max(self.finish_times[-1], request.arrival_time) if self.finish_times else request.arrival_time
        finish_time = start_time + request.process_time
        self.finish_times.append(finish_time)
        return Response(False, start_time)

    def process(self, request):
        if len(self.finish_times) < self.size:
            return self.process_with_buffer(request)
        else:
            self.update(request.arrival_time)
            if len(self.finish_times) < self.size:
                return self.process_with_buffer(request)
            else:
                return Response(True, -1)


def read_requests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(
            Request(arrival_time, process_time)
        )
    return requests


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def print_responses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)


if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = read_requests(count)

    buffer = Buffer(size)
    responses = process_requests(requests, buffer)

    print_responses(responses)
