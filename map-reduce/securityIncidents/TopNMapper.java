package org.bits.mr;

import java.io.*;
import java.util.*;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.mapreduce.Mapper;


public class TopNMapper extends Mapper<Object, Text, Text, LongWritable> {

    private TreeMap<Long, String> topIncidentsMap;

    @Override
    public void setup(Context context) {
        topIncidentsMap = new TreeMap<>();
    }

    @Override
    public void map(Object key, Text value, Context context) {
        String[] tokens = value.toString().split("\t");

        String locality = tokens[0];
        long incidentCount = Long.parseLong(tokens[1]);
        topIncidentsMap.put(incidentCount, locality);

        if (topIncidentsMap.size() > 10) {
            topIncidentsMap.remove(topIncidentsMap.firstKey());
        }
    }

    @Override
    public void cleanup(Context context) throws IOException,
            InterruptedException {
        for (Map.Entry<Long, String> entry : topIncidentsMap.entrySet()) {
            long count = entry.getKey();
            String locality = entry.getValue();
            context.write(new Text(locality), new LongWritable(count));
        }
    }
}
