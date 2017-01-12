# HL7 translation exercise

HL7 is a standard used to share patient data between hospital systems. In this exercise, you will be required to extract data from raw messages and produce normalized output objects that could be consumed by downstream systems.


## The problem

Given a JSON-encoded object containing this message:

<pre>MSH|^~\\&|HL7|VITALS|EXAMPLE HOSPITAL||201701120900||ORU^R01|53b3cd1ea11b448ebf99656f637e54e3|P|2.3||||||UNICODE UTF-8
PID|||<strong style="color:#f00;font-weight:normal">40724907</strong>^^^A^MR||
PV1||E|STIC^STIC^01^^^^EXAMPLE HOSPITAL
OBR|1||||||<strong style="color:#f00;font-weight:normal">20170112000800</strong>
OBX|1|ST|^<strong style="color:#f00;font-weight:normal">SBP</strong>^^8480-6^Systolic blood pressure^LN||<strong style="color:#f00;font-weight:normal">154</strong>|<strong style="color:#f00;font-weight:normal">mm(hg)</strong>||R
OBX|2|ST|^<strong style="color:#f00;font-weight:normal">HR</strong>^^8886-4^Heart rate^LN||<strong style="color:#f00;font-weight:normal">99</strong>|<strong style="color:#f00;font-weight:normal">beats/min</strong>||R
OBX|3||^<strong style="color:#f00;font-weight:normal">MBP</strong>^^8478-0^Mean blood pressure^LN||<strong style="color:#f00;font-weight:normal">120</strong>|<strong style="color:#f00;font-weight:normal">mm(hg)</strong>||R
OBX|4|ST|^<strong style="color:#f00;font-weight:normal">CVP3</strong>^^8591-0^Central venous pressure (CVP) Mean^LN||<strong style="color:#f00;font-weight:normal">13</strong>|<strong style="color:#f00;font-weight:normal">mm(hg)</strong>||R
OBX|5|ST|^<strong style="color:#f00;font-weight:normal">DBP</strong>^^8462-4^Diastolic blood pressure^LN||<strong style="color:#f00;font-weight:normal">103</strong>|<strong style="color:#f00;font-weight:normal">mm(hg)</strong>||R
OBX|6|ST|^<strong style="color:#f00;font-weight:normal">SPO2-%</strong>^^20081-6^Pulse oximetry site^LN||<strong style="color:#f00;font-weight:normal">96</strong>|<strong style="color:#f00;font-weight:normal">%</strong>||R
OBX|7|ST|^<strong style="color:#f00;font-weight:normal">RR</strong>^^9279-1^Respiratory rate^LN||<strong style="color:#f00;font-weight:normal">16</strong>|<strong style="color:#f00;font-weight:normal">breaths/min</strong>||R</pre>

Produce this output:

    {"event":"SBP","patient":"40724907","time":"2017-01-12T00:08:00Z","unit":"mm(hg)","value":154}
    {"event":"HR","patient":"40724907","time":"2017-01-12T00:08:00Z","unit":"beats/min","value":99}
    {"event":"MBP","patient":"40724907","time":"2017-01-12T00:08:00Z","unit":"mm(hg)","value":120}
    {"event":"CVP3","patient":"40724907","time":"2017-01-12T00:08:00Z","unit":"mm(hg)","value":13}
    {"event":"DBP","patient":"40724907","time":"2017-01-12T00:08:00Z","unit":"mm(hg)","value":103}
    {"event":"SPO2-%","patient":"40724907","time":"2017-01-12T00:08:00Z","unit":"%","value":96}
    {"event":"RR","patient":"40724907","time":"2017-01-12T00:08:00Z","unit":"breaths/min","value":16}

The `messages.ldjson` input file contains 10 JSON-encoded message objects, each on its own line. Extract each observation in every message and append an event to your output with the required attributes. The raw message text is available as the `text` key in the message object.

Each output line corresponds to an `OBX` line in the original message and describes an individual observation of the patient. The `OBR` line in the message contains data pertaining to all subsequent `OBX` lines, so some fields will be repeated in each output line. The patient can be identified using a field in the `PID` line.


## The solution

Each JSON-encoded output object must be written to a single line, with each line separated by a newline (`\n`) character. It's acceptable to include blank lines in your output, as well as comment lines with a leading `#` character.

Note that message lines displayed in this document are separated by newlines (`\n`), while lines in the real messages are separated by carriage returns (`\r`).

For the purposes of this exercise, it's safe to make the following assumptions:

  * The message text encoding is UTF-8
  * All times are in UTC
  * Messages will only contain one `OBR` segment
  * All required values will be present in the message

Your output objects must have the following fields:

  * `event` is a a string identifying the kind of observation
  * `patient` is an 8-digit string that uniquely identifies a patient
  * `time` is a string containing the ISO8601-encoded time when the observation occurred
  * `unit` is a string containing the relevant unit of measure
  * `value` is an integer containing an observed measurement

Save your work in a clone of this repository. You aren't required to use any particular programming language for this exercise, but Python is a good idea if you're up for it. We're a Python shop and you will be expected to learn the language if you don't already know it. Be sure to update this document with instructions on how to run your solution. Submit a pull request on GitHub when you're ready to have us take a look.
