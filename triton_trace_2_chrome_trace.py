import json


def parse_triton_trace(triton_trace_file):
    with open(triton_trace_file, 'r') as f:
        triton_events = json.load(f)
    return triton_events


def convert_to_chrome_trace(triton_events):
    chrome_trace_events = []

    for event in triton_events:
        if 'timestamps' not in event:
            continue
        name = event['timestamps'][0]['name']
        if name == "HTTP_RECV_START":
            ph = "b"
        elif name == "HTTP_SEND_END":
            ph = "e"
        else:
            continue

        chrome_event = {
            'cat': "resnet50",
            'name': str(event['id']),
            'id': str(event['id']),
            'ph': ph,
            # convert to micro second
            'ts': event['timestamps'][0]['ns'] * 0.001,
            # TODO: add exact value
            'pid': 0,
        }
        chrome_trace_events.append(chrome_event)
    return chrome_trace_events


def write_chrome_trace(chrome_trace_events, output_file):
    with open(output_file, 'w') as f:
        json.dump(chrome_trace_events, f)


triton_trace_file = 'triton_trace.json'  # replace with your Triton trace file
chrome_trace_file = 'chrome_trace.json'  # replace with your output file

triton_events = parse_triton_trace(triton_trace_file)
chrome_trace_events = convert_to_chrome_trace(triton_events)
write_chrome_trace(chrome_trace_events, chrome_trace_file)
