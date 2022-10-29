package org.bits.mr;

import java.io.IOException;
import java.util.Map;
import java.util.TreeMap;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;


public class TopNReducer extends Reducer<Text, LongWritable, LongWritable, Text> {

    private TreeMap<Long, String> topNMap;

    @Override
    public void setup(Context context) {
        topNMap = new TreeMap<>();
    }

    @Override
    public void reduce(Text key, Iterable<LongWritable> values, Context context) {

        String locality = key.toString();
        long incidents = 0;

        for (LongWritable val : values) {
            incidents = val.get();
        }

        topNMap.put(incidents, locality);

        if (topNMap.size() > 10) {
            topNMap.remove(topNMap.firstKey());
        }
    }

    @Override
    public void cleanup(Context context) throws IOException,
            InterruptedException {
        for (Map.Entry<Long, String> entry : topNMap.entrySet()) {
            long incidents = entry.getKey();
            String locality = entry.getValue();
            context.write(new LongWritable(incidents), new Text(locality));
        }
    }
}